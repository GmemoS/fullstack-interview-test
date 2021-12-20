import React from "react";
import { Link } from "react-router-dom";

export function CommitsList({branch, commits}) {
    return (
        <div>
            <center><h1>Commits in {branch}</h1></center>
            {commits.map((commit) => (
                <Link to={{
                    pathname: "/commit",
                    search: "?id="+commit.hexsha
                }}>
                    <div className="card" key={commit.hexsha}>
                        <div className="card-body">
                            <p className="card-title">{commit.hexsha}</p>
                            <p className="card-text">{commit.message}</p>
                            <p className="card-text">{commit.author}</p>
                            <p className="card-text">{commit.datetime}</p>
                        </div>
                    </div>
                </Link>
            ))}
        </div>
    );
}
