import React, { useState, useEffect } from "react";
import { BrachesList } from "./BranchesList";

export function Branches() {
    const [branches, setBranches] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/api/v1/branches')
        .then(resp => resp.json())
        .then(data => setBranches(data))
        .catch(error => console.log(error));
    });

    return (
        <BrachesList branches={branches} />
    );
}
