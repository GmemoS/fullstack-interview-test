import React from "react";
import { Link } from "react-router-dom";

export function BrachesList({branches}) {
    return (
        <div>
            <center><h1>Branches</h1></center>
            {branches.map((branch) => (
                <Link to={{
                    pathname: "/branch",
                    search: "?name="+branch.name
                }}>
                    <div className="card" key={branch.name}>
                        <div className="card-body">
                            <p className="card-title">{branch.name}</p>
                            <p className="card-text">{branch.commit}</p>
                            <p className="card-text">{branch.datetime}</p>
                        </div>
                    </div>
                </Link>
            ))}
        </div>
    );
}
