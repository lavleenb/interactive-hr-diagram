import Plot from "react-plotly.js";

export const SamplePlot = () => {
    const plot = [{
        x: [1,2,3,4,5],
        y: [3,4,6,9,10],
        type: 'scatter',
        marker: {color: 'green'},
    }];
    return (
        <Plot
            data={plot}
            layout={ {width: 500, height: 500} }

        />
    );
};