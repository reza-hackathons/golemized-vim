FROM golemfactory/base:1.8

RUN apt-get update 

RUN apt-get install -y gcc libc-dev make acl-dev libncurses-dev curl unzip
RUN mkdir /golem/vim
RUN curl https://codeload.github.com/vim/vim/zip/master -o /golem/vim/vim.zip
RUN unzip -q /golem/vim/vim.zip -d /golem/vim/vim-src

VOLUME /golem/work /golem/output /golem/resources
