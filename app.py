import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

########### Define your variables ######
myheading1 = 'Sf Bay Area - Invest in Living'
image1 = 'sf_houses.jpeg'
tabtitle = 'SF Bay Area Housing'
sourceurl = 'http://jse.amstat.org/v19n3/decock.pdf'
githublink = 'https://github.com/ksebastian/data-science-regression'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div([
        html.Img(src=app.get_asset_url(image1), style={'width': '30%', 'height': 'auto'}, className='four columns'),
        html.Div([
            html.H3('Features of Home:'),
            html.Div('Bedrooms:'),
            dcc.Input(id='Bedrooms', value=2, type='number', min=1, max=5, step=1),
            html.Div('Bathrooms:'),
            dcc.Input(id='Bathrooms', value=4, type='number', min=1, max=5, step=1),
            html.Div('Total Square Feet:'),
            dcc.Input(id='TotalSF', value=2000, type='number', min=100, max=15000, step=1),
            html.Div('Lot Size:'),
            dcc.Input(id='LotSize', value=2000, type='number', min=100, max=25000, step=1),
            html.Div('School Score:'),
            dcc.Input(id='SchoolScore', value=0, type='number', min=0, max=100, step=1),
            html.Div('Commute Time:'),
            dcc.Input(id='CommuteTime', value=0, type='number', min=0, max=300, step=1),
        ], className='four columns'),
        html.Div([
            html.Button(children='Submit', id='submit-val', n_clicks=0,
                        style={
                            'background-color': 'red',
                            'color': 'white',
                            'margin-left': '5px',
                            'verticalAlign': 'center',
                            'horizontalAlign': 'center'}
                        ),
            html.H3('Predicted Home Value:'),
            html.Div(id='Results')
        ], className='four columns')
    ], className='twelve columns',
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.H4('Regression Equation:'),
    html.Div(
        'Predicted Price = 1193255.55 + -54313*Beds + 94041*Baths + 311452*Home_size + 110345*Lot_size + 172126*School_score + -405207*Commute_time'),
    html.Br(),
    html.A('Google Spreadsheet',
           href='https://docs.google.com/spreadsheets/d/1q2ustRvY-GcmPO5NYudvsBEGNs5Na5p_8LMeS4oM35U/edit?usp=sharing'),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
]
)


# Equation:  y =  1193255.55 +
#                 -54313*Beds +
#                 94041*Baths +
#                 311452*Home_size +
#                 110345*Lot_size +
#                 172126*School_score +
#                 -405207*Commute_time

######### Define Callback
@app.callback(
    Output(component_id='Results', component_property='children'),
    Input(component_id='submit-val', component_property='n_clicks'),
    State(component_id='Bedrooms', component_property='value'),
    State(component_id='Bathrooms', component_property='value'),
    State(component_id='TotalSF', component_property='value'),
    State(component_id='LotSize', component_property='value'),
    State(component_id='SchoolScore', component_property='value'),
    State(component_id='CommuteTime', component_property='value')

)
def ames_lr_function(clicks, Bedrooms, Bathrooms, TotalSF, LotSize, SchoolScore, CommuteTime):
    if clicks == 0:
        return "waiting for inputs"
    else:
        print(f"Bedrooms={Bedrooms}, Bathrooms={Bathrooms}, TotalSF={TotalSF}, LotSize={LotSize}, SchoolScore={SchoolScore}, CommuteTime={CommuteTime}")
        y = [1193255.55 + -54313 * Bedrooms + 94041 * Bathrooms + 311452 * TotalSF + 110345 * LotSize + 172126 * SchoolScore + -405207 * CommuteTime]
       # y = [1193255.55 + -54313 * 0.674479 + 94041 * -0.378585 + 311452 * -0.057289 + 110345 * -0.305219 + 172126 * -1.116443 + -405207 * 1.027323]

        formatted_y = "${:,.2f}".format(y[0])
        return formatted_y


############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
