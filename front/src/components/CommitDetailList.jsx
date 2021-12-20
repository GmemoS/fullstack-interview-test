import React from "react";
import { Link } from "react-router-dom";

export function CommitDetailList({commit, detail}) {
    return (
        <div>
            <center><h1>Commit Detail</h1></center>
            <div className="card" key={detail.hexsha}>
                <div className="card-body">
                    <p className="card-title">{commit}</p>
                    <p className="card-text">{detail.message}</p>
                    <p className="card-text">{detail.author} &lt;{detail.email}&gt;</p>
                    <p className="card-text">{detail.datetime}</p>
                    <p className="card-text">{detail.count_files} file(s) changed</p>
                </div>
            </div>
        </div>
    );
}
