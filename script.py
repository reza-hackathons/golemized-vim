import asyncio

from yapapi.log import enable_default_logger, log_summary, log_event_repr # noqa
from yapapi.runner import Engine, Task, vm
from yapapi.runner.ctx import WorkContext
from datetime import timedelta


async def main(subnet_tag = "testnet"):
    package = await vm.repo(
        image_hash = "8af7ca292da9c81d5c7193b76794b6143b3b13cead94b115efb91e57",
        min_mem_gib = 0.5,
        min_storage_gib = 2.0,
    )

    async def worker(ctx: WorkContext, tasks):
        async for task in tasks:
            ctx.run("/bin/bash", "-c", "cp -r /golem/vim/vim-src/vim-master /golem/work/vim; cd /golem/work/vim; make -j4 >> /golem/output/log.txt 2>&1")
            output_file = f"out/vim"
            ctx.download_file(f"/golem/work/vim/src/vim", output_file)
            ctx.download_file(f"/golem/output/log.txt", f"out/log.txt")
            yield ctx.commit()
            task.accept_task(result=output_file)

        ctx.log(f"yay, vim finally got compiled.")

    jobs: range = range(0, 1, 1)
    init_overhead: timedelta = timedelta(minutes = 3)
    async with Engine(
        package = package,
        max_workers = 1,
        budget = 1000,
        timeout = init_overhead + timedelta(minutes = 3),
        subnet_tag = subnet_tag,
        event_emitter = log_summary(log_event_repr),
    ) as engine:

        async for job in engine.map(worker, [Task(data = job) for job in jobs]):
            print(f"[job done: {job}, result: {job.output}")


enable_default_logger()
loop = asyncio.get_event_loop()
job = loop.create_task(main(subnet_tag = "devnet-alpha.2"))
try:
    asyncio.get_event_loop().run_until_complete(job)
except (Exception, KeyboardInterrupt) as e:
    print(e)
    job.cancel()
    asyncio.get_event_loop().run_until_complete(job)
