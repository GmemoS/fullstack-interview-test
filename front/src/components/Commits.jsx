import React, { useState, useEffect } from "react";
import { useSearchParams } from "react-router-dom"
import { CommitsList } from "./CommitsList";

export function Commits() {
    const [searchParams, setSearchParams] = useSearchParams();
    const branchName = searchParams.get('name');

    const [commits, setCommits] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/api/v1/commits?branch_name='+encodeURIComponent(branchName))
        .then(resp => resp.json())
        .then(data => setCommits(data))
        .catch(error => console.log(error));
    });

    return (
        <CommitsList branch={branchName} commits={commits} />
    );
}
