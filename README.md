# golemized-vim  
A golemized docker image for compiling the most loved vim editor.  
## Steps
1. Make sure you have docker installed.  
- `cd golem-vim-docker`  
- `docker build -t YOUR-USERNAME/golem-vim:YOUR-TAG .`  
- `docker push YOUR-USERNAME/golem-vim:YOUR-TAG`  
2. Golemize the docker image.  
- `python3 -m venv SOME-VIRTUAL-ENV-NAME`  
- `source SOME-VIRTUAL-ENV-NAME/bin/activate`  
- `pip3 install -U pip`  
- `pip3 install yapapi certifi gvmkit-build`  
- `gvmkit-build YOUR-USERNAME/golem-vim:YOUR-TAG`  
- `gvmkit-build YOUR-USERNAME/golem-vim:YOUR-TAG --push`
- `Save the returned hash and put it into the script.py`   
3. Ask the providers to compile.  
- Open a new terminal: `yagna service run`  
- Open a new terminal: `export YAGNA-APPKEY = YOUR-YAGNA-APPKEY`  
- `yagna payment init -r`  
- `python script.py`  
4. Run the compiled Vim!  
- `cd out`  
- `chmod +x vim`  
- `./vim`

## Demo  
[https://youtu.be/ougeYENjLbs](https://youtu.be/ougeYENjLbs)