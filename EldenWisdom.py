#!.venv/bin/python
import gradio as gr
import csv

title="Elden Wisdom App"

theme = gr.themes.Glass(
    primary_hue="gray",
    neutral_hue="sky",
    text_size="lg",
    font=[gr.themes.GoogleFont('Cinzel'), 'Candara', 'Noto Sans', 'source-sans-pro'],
)

def load_runes():
    _all_stones = []
    with open('runes.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            _all_stones.append(row)
    return _all_stones

def load_levels():
    _levels = dict()
    with open('eldenring_levels.csv') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:
                _levels[int(row[0])] = int(row[3].replace(",",""))
    return _levels

def load_farming():
    farmingDict = dict()
    with open('farming.csv') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:
                farmingDict[row[0]] = int(row[1])
    return farmingDict

def levelCalc(start, desired, farming_choice):
    _msg = ""
    _levels = load_levels()
    _farming = load_farming()
    exp_start = _levels.get(int(start))
    exp_desired = _levels.get(int(desired))
    _exp = exp_desired - exp_start
    if desired > start:
        _msg += f"To go from Lv{start} to Lv{desired} will take {_exp:,} runes."
        if farming_choice:
            _nexp = _farming.get(farming_choice)
            _fk = round(_exp/_nexp, 0) + 1
            _msg += f"\n\nYou'll need to slay {_fk:,.0f} of {farming_choice} to get this amount."
    else: 
        _msg += f"\nPlease re-adjust the slider to have the desired level be higher than your current level."

    return _msg
        


def calculate(
        CurrentExp,
        GoldenRune_1, 
        GoldenRune_2,
        GoldenRune_3,
        GoldenRune_4,
        GoldenRune_5,
        GoldenRune_6,
        GoldenRune_7,
        GoldenRune_8,
        GoldenRune_9,
        GoldenRune_10,
        GoldenRune_11,
        GoldenRune_12,
        GoldenRune_13,
        HeroRune_1,
        HeroRune_2,
        HeroRune_3,
        HeroRune_4,
        HeroRune_5,
        LordRune):
    data = load_runes()
    #print(tabulate.tabulate(data, headers='firstrow', tablefmt='simple'))
    _g1_exp = int(GoldenRune_1) * int(data[1][1])
    _g2_exp = int(GoldenRune_2) * int(data[2][1])
    _g3_exp = int(GoldenRune_3) * int(data[3][1])
    _g4_exp = int(GoldenRune_4) * int(data[4][1])
    _g5_exp = int(GoldenRune_5) * int(data[5][1])
    _g6_exp = int(GoldenRune_6) * int(data[6][1])
    _g7_exp = int(GoldenRune_7) * int(data[7][1])
    _g8_exp = int(GoldenRune_8) * int(data[8][1])
    _g9_exp = int(GoldenRune_9) * int(data[9][1])
    _g10_exp = int(GoldenRune_10) * int(data[10][1])
    _g11_exp = int(GoldenRune_11) * int(data[11][1])
    _g12_exp = int(GoldenRune_12) * int(data[12][1])
    _g13_exp = int(GoldenRune_13) * int(data[13][1])
    _h1_exp = int(HeroRune_1) * int(data[14][1])
    _h2_exp = int(HeroRune_2) * int(data[15][1])
    _h3_exp = int(HeroRune_3) * int(data[15][1])
    _h4_exp = int(HeroRune_4) * int(data[16][1])
    _h5_exp = int(HeroRune_5) * int(data[17][1])
    _lr_exp = int(LordRune) * int(data[18][1])
    _summed_exp = \
        int(CurrentExp) + \
        int(_g1_exp) + \
        int(_g2_exp) + \
        int(_g3_exp) + \
        int(_g4_exp) + \
        int(_g5_exp) + \
        int(_g6_exp) + \
        int(_g7_exp) + \
        int(_g8_exp) + \
        int(_g9_exp) + \
        int(_g10_exp) + \
        int(_g11_exp) + \
        int(_g12_exp) + \
        int(_g13_exp) + \
        int(_h1_exp) + \
        int(_h2_exp) + \
        int(_h3_exp) + \
        int(_h4_exp) + \
        int(_h5_exp) + \
        int(_lr_exp)
    if int(CurrentExp) > 0: return f"Your selected runes, with your {CurrentExp:,} experience, will add up to a total of {_summed_exp:,} experience points."
    else: return f"Your Selected runes will add up to {_summed_exp:,} experience."
    #return tabulate.tabulate(data, headers='firstrow', tablefmt='simple')

with gr.Blocks(theme=theme, title=title, show_api=False) as eldenWisdom:
    gr.Markdown("# " + title)
    gr.Markdown("### Please find the tabs below to help inform you about necessities in Elden Ring.")
    with gr.Tab("RUNES"):
        with gr.Row():
            with gr.Column():
                fn=calculate
                inputs=[
                    gr.Number(label="Current Experience", value=0), #CurrentExp
                    gr.Slider(label="Golden Rune 1s", value=0, minimum=0, maximum=50, step=1), #GoldenRune_1,
                    gr.Slider(label="Golden Rune 2s", value=0, minimum=0, maximum=50, step=1), #GoldenRune_2,
                    gr.Slider(label="Golden Rune 3s", value=0, minimum=0, maximum=50, step=1), #GoldenRune_3,
                    gr.Slider(label="Golden Rune 4s", value=0, minimum=0, maximum=50, step=1), #GoldenRune_4,
                    gr.Slider(label="Golden Rune 5s", value=0, minimum=0, maximum=50, step=1), #GoldenRune_5,
                    gr.Slider(label="Golden Rune 6s", value=0, minimum=0, maximum=50, step=1), #GoldenRune_6,
                    gr.Slider(label="Golden Rune 7s", value=0, minimum=0, maximum=50, step=1), #GoldenRune_7,
                    gr.Slider(label="Golden Rune 8s", value=0, minimum=0, maximum=50, step=1), #GoldenRune_8,
                    gr.Slider(label="Golden Rune 9s", value=0, minimum=0, maximum=50, step=1), #GoldenRune_9,
                    gr.Slider(label="Golden Rune 10s", value=0, minimum=0, maximum=50, step=1), #GoldenRune_10,
                    gr.Slider(label="Golden Rune 11s", value=0, minimum=0, maximum=50, step=1), #GoldenRune_11,
                    gr.Slider(label="Golden Rune 12s", value=0, minimum=0, maximum=50, step=1), #GoldenRune_12,
                    gr.Slider(label="Golden Rune 13s", value=0, minimum=0, maximum=50, step=1), #GoldenRune_13,
                    gr.Slider(label="Hero Rune 1s", value=0, minimum=0, maximum=20, step=1), #HeroRune_1,
                    gr.Slider(label="Hero Rune 2s", value=0, minimum=0, maximum=20, step=1), #HeroRune_2,
                    gr.Slider(label="Hero Rune 3s", value=0, minimum=0, maximum=20, step=1), #HeroRune_3,
                    gr.Slider(label="Hero Rune 4s", value=0, minimum=0, maximum=20, step=1), #HeroRune_4,
                    gr.Slider(label="Hero Rune 5s", value=0, minimum=0, maximum=20, step=1), #HeroRune_5,
                    gr.Slider(label="Lord Runes", value=0, minimum=0, maximum=10, step=1), #LordRune,
                ]
                
            with gr.Column():
                gr.TextArea(label="How to Use", value="Enter your existing experience, and the amount of runes you want to use, to find out if you have enough runes. \n\nSkip entering any experience (and just use the sliders) to just find out how much your runes add up to. \n\nThe Levels tab can inform you how many runes you need to level up to your desired level.")
                outputs=[gr.Textbox(label="Output", lines=2)]
                submit = gr.Button("Submit")
                submit.click(fn, inputs, outputs)

    with gr.Tab("LEVELS"):
        fn=levelCalc
        with gr.Row():
            with gr.Column():
                inputs=[
                    gr.Slider(label="Starting Level", value=20, minimum=1, maximum=712, step=1),
                    gr.Slider(label="Desired Level", value=25, minimum=1, maximum=713, step=1),
                    gr.Radio(choices=load_farming().keys(), label="Farming Choice"),
                ]
            with gr.Column():
                gr.TextArea(label="How to Use", value="This section is meant to show how much experience you need to go from one level to the one you'd like to be at.")
                outputs=[gr.Textbox(label="Output", lines=2)]
                submit = gr.Button("Submit")
                submit.click(fn, inputs, outputs)
    with gr.Tab("INFO"):
        _msg = "This application utilizes the work tirelylessly completed by the authors of the EldenRing Wiki page on Fextalife. \n\nHere is the direct link: https://eldenring.wiki.fextralife.com/Golden+Runes. \n\nThe data used from here is namely on one of the Golden Rune pages, it's  a table that's been converted into memory for this application. \n\n There is also a second page on this wiki that has done the same for leveling information, which was cut up by this application and stored in memory for calculations on the Levels tab. \n\n Here is the link: https://eldenring.wiki.fextralife.com/Level. \n\n Thanks to all who did this work prior!"
        gr.TextArea(label="Data Used", interactive=False,value=_msg, lines=15)

#eldenWisdom.launch(share=False, show_api=False, enable_monitoring=False, inbrowser=True, debug=False) 
