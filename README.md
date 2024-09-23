## How to Run

This is should work on Linux, may need something slightly different for other OS.  I have only tested on Linux. 

Git clone the repository. 

Create a python virtual environment.

```sh
sudo python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For pyautogui it requires 

You must install tkinter on Linux to use MouseINfo.

```sh
sudo apt-get install python3-tk python3-dev
```

Generate the graph data

```sh
cd graph
python directed_graph_generator.py
```

Run the streamlit app

```sh
streamlit run directed_graph_viz.py
```