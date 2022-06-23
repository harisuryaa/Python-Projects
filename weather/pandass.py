import lxml as lxml
import pandas as pd
h= pd.read_html("https://stats.espncricinfo.com/ci/engine/player/931581.html?class=2;template=results;type=allround;view=innings")
print(h)