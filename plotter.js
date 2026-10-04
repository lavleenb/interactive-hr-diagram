var trace1 = {
  x: [1, 2, 3, 4],
  y: [10, 15, 13, 17],
  mode: 'markers',
  type: 'scatter'
};

var trace2 = {
  x: [2, 3, 4, 5],
  y: [16, 5, 11, 9],
  mode: 'lines',
  type: 'scatter'
};

var trace3 = {
  x: [1, 2, 3, 4],
  y: [12, 9, 15, 12],
  mode: 'lines+markers',
  type: 'scatter'
};

var layout = {
    title: {
        text: 'A Temporary Graph',
    },
    autosize: false,
    width: screen.width - 50,
    height: 600,
    margin: {
        l: 50,
        r: 50,
        b: 100,
        t: 100,
        pad: 4,
    },
    paper_bgcolor: '#000',
    plot_bgcolor: '#000000',
    font: {
        family: 'Arial',
        color: '#fff',
    }
}

var data = [trace1, trace2, trace3];

Plotly.newPlot('plotly-scatterplot', data, layout);