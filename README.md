# Install

## Node
### [Volta](https://volta.sh)

```sh
curl https://get.volta.sh | bash

volta install node
npm install -g neovim
```

PATHを確認(.bashrc)

## Python

### pipx 

```sh
sudo apt install pipx
pipx install pynvim 
pipx install autopep8 
pipx install flake8 
pipx install black 
pipx install isort
```

PATHを確認($HOME/.local/bin)

##  Neovim

### [gh](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)

```sh
(type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y)) \
	&& sudo mkdir -p -m 755 /etc/apt/keyrings \
	&& out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
	&& cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& sudo mkdir -p -m 755 /etc/apt/sources.list.d \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& sudo apt update \
	&& sudo apt install gh -y
```

#### gh settings
```sh
gh
gh config set editor nvim
```
### [config](https://github.com/omas-public/nvim.git)

```sh
git clone https://github.com/omas-public/nvim.git ~/.config/nvim
```

### [Neovim](https://github.com/neovim/neovim/blob/master/INSTALL.md)

```sh
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux-x86_64.appimage
chmod u+x nvim-linux-x86_64.appimage
sudo mv nvim-linux-x86_64.appimage /usr/local/nvim
```

### clipboard

```sh
echo $XDG_SESSION_TYPE
```
結果がx11なら ```sudo apt install xclip``` Waylandなら ```sudo apt install wl-clipboard```

### Gist

```sh
nvim
:GistCreate
```

### [Copilot](https://github.com/github/copilot.vim/blob/release/README.md) 

```sh
git clone --depth=1 https://github.com/github/copilot.vim.git \
  ~/.config/nvim/pack/github/start/copilot
```

#### setup

```sh
nvim
:Copilot setup
```
