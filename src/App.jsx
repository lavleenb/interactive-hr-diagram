import './App.css'
import { Header } from './Header'
import { Info } from './Info'
import { SamplePlot } from './SamplePlot'

function App() {

  return (
    <>
      <Header />
      <section>
        <SamplePlot />
      </section>
      <br/>
      <section>
        <Info />
        <h1>poopy.</h1>
        <p>poopy scoopy.</p>
      </section>
    </>
  )
}

export default App
