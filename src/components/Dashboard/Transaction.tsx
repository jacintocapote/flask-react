"use client";
import React, { useState } from 'react';
import TableTransaction from "../Tables/TableTransaction"
import FormTransaction from "../FormElements/TransactionForm"

const Transaction: React.FC = () => {
  const [count, setCount] = useState(0);

  // Function to reload/re-render the ReloadedComponent
  const reloadData = () => {
    setCount((prevCount) => prevCount + 1);  // Update state
  };

  return (
    <>
      <div className="mt-4 grid grid-cols-12 gap-4 md:mt-6 md:gap-6 2xl:mt-9 2xl:gap-7.5">
        <div className="col-span-12 xl:col-span-12">
          <TableTransaction count={count} />
          <FormTransaction reloadData={reloadData} />
        </div>
      </div>
    </>
  );
};

export default Transaction;