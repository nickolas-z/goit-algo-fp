import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np

# Приклад даних
frame = np.random.rand(100, 100)  # Випадкова матриця

# Ініціалізуємо додаток Dash
app = dash.Dash(__name__)

# Створюємо графік із Plotly
fig = px.imshow(frame)
fig.update_xaxes(showticklabels=True, title_text=f"Width: {frame.shape[1]}px")
fig.update_yaxes(showticklabels=True, title_text=f"Height: {frame.shape[0]}px")
fig.update_layout(autosize=False, width=500, height=500, coloraxis_showscale=True)

# Описуємо структуру додатку
app.layout = html.Div(
    [dcc.Graph(id="interactive-plot", figure=fig), html.Div(id="output-div")]
)


# Визначаємо callback для взаємодії з графіком
@app.callback(Output("output-div", "children"), Input("interactive-plot", "clickData"))
def on_click(clickData):
    if clickData is not None:
        # Тут можна викликати вашу Python функцію
        x = clickData["points"][0]["x"]
        y = clickData["points"][0]["y"]
        return f"You clicked on point: (x={x}, y={y})"
    return "Click on the graph to see the coordinates."


# Запускаємо додаток
if __name__ == "__main__":
    app.run_server(debug=True)
