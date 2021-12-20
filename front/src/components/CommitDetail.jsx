import React, { useState, useEffect } from "react";
import { useSearchParams } from "react-router-dom"
import { CommitDetailList } from "./CommitDetailList";

export function CommitDetail() {
    const [searchParams, setSearchParams] = useSearchParams();
    const commitId = searchParams.get('id');

    const [detail, setDetail] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/api/v1/commits?id='+encodeURIComponent(commitId))
        .then(resp => resp.json())
        .then(data => setDetail(data))
        .catch(error => console.log(error));
    });

    return (
        <CommitDetailList commit={commitId} detail={detail} />
    );
}
