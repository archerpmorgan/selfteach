import React, { useState } from 'react';
import { MenuItems } from "./MenuItems";
import './Navbar.css';
import { Link } from 'react-router-dom';


function Navbar() {

    const [clicked, setClicked] = useState(false);

    const navStyleSignedIn = {
            color: "black",
            fontFamily: "Palatino",
            textDecoration: 'none',
            padding: "0.5rem 1rem"
    };

    return (
        <nav className="NavbarItems">

            <h1 className="navbar-logo">Selfteach</h1>

            <div className="menu-icon" onClick={ () => setClicked( !clicked )}>
                <i className={clicked ? 'fas fa-times' : 'fas fa-bars'}></i>
            </div>

            <ul className={clicked ? 'nav-menu active' : 'nav-menu'}>
                {MenuItems.map((item, index) => {
                    return (
                        <Link key={index} to={`/${clean(item.title)}`} style={navStyleSignedIn}>
                            <li>
                                {item.title}
                                <i className={item.icon} ></i>
                            </li>
                        </Link>
                    )
                })}
                <NavButton/>
            </ul>
        </nav>
    );
}


function NavButton() {

    const data = {
        title: 'Sign up',
        url: '#',
        cName: 'nav-links-mobile'
    }
    
    return (
        <li>
            <a className={data.cName} href={data.url}>
            {data.title}
            <i className={data.icon}></i>
            </a>
        </li>
    );
}

// strip spaces and lowercase
function clean( name ) {
    return name.toLowerCase().replace(/\s/g, '')
}

export default Navbar