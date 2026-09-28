import { Expression } from "algebra.js";

export const Info = () => {
    const x = new Expression("x");
    const y = new Expression("y");
    const L_sun = new Expression("L_\\odot");
    return (
        <>
            <h1>what is a hertzprung-russell diagram?</h1>
            <p>
                The Hertzprung-Russel, or H-R, Diagram plots the luminosity-temperature relationship
                of stars. The {x}-axis is the stellar surface temperature in Kelvins,
                which can also be thought of as the star's OBAFGKM classification. The {y}-axis
                is the star's absolute magnitude, or luminosity, in units of Solar luminosity ({L_sun}).
            </p>
        </>
    );
}