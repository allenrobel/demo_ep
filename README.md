# Smart Endpoints Demo

Demo for "smart" endpoints implementation.  Probably of zero interest for anyone other than those I've already shared with.

## Usage

```bash
cd $HOME/repos
git clone https://github.com/allenrobel/demo_ep.git
cd demo_ep
python -m venv .venv --prompt demo_ep
source .venv/bin/activate
source env
pip install uv
uv sync
pytest # run unit tests
python demo_composite.py # run demo script
```
