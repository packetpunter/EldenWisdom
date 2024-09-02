from fastapi import FastAPI
import gradio as gr
app = FastAPI()
from EldenWisdom import eldenWisdom
app = gr.mount_gradio_app(app, eldenWisdom, path="/")