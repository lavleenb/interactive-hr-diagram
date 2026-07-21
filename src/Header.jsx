import styles from "./Header.module.css"

export const Header = () => {
    return (
        <header>
            <nav className={`${styles.navbar}`}>
                <ul className={`${styles.navlist}`}>
                    <li>home.</li>
                    <li>about.</li>
                </ul>
            </nav>
            <h1>interactive hertzprung-russell diagram.</h1>
        </header>
    )
}