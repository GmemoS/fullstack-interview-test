import React from "react";
import { NavLink } from "react-router-dom";

export function Navigation() {
  return (
    <div className="navigation">
      <nav className="navbar navbar-expand navbar-dark bg-dark">
        <div className="container">
          <NavLink className="navbar-brand" to="/">
            Git Manager
          </NavLink>
          <div>
            <ul className="navbar-nav ml-auto">
              <li className="nav-item">
                <NavLink className="nav-link" to="/">
                  Branches
                  <span className="sr-only">(current)</span>
                </NavLink>
              </li>
              {/* <li className="nav-item">
                <NavLink className="nav-link" to="/pr">
                  Pull Requests
                </NavLink>
              </li> */}
            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
}
