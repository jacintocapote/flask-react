"use client";
import React, { useState } from 'react';
import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb";
import {createTransaction} from "@/api/transactions";
import AlertError from '../Alerts/AlertError';
import AlertSuccess from '../Alerts/AlertSuccess';

const TransactionForm:  React.FC<{ reloadData: () => void }> = ({ reloadData }) => {

  const [id, setId] = useState<string>('');
  const [transactionType, setTransactionType] = useState<string>('');
  const [amount, setAmount] = useState<string>('');
  const [currency, setCurrency] = useState<string>('');
  const [bankAccountId, setBankAccountId] = useState<string>('');
  const [error, setError] = useState<string>('');
  const [message, setMessage] = useState<string>('');

  const addItem = () => {
    if (id && transactionType && amount && currency && bankAccountId) {
      createTransaction(id, transactionType, currency, amount, bankAccountId)
      .then(data => {
        if (data == "Error") {
          setError("Error creating the transaction.")
          setMessage("")
        }
        else {
          reloadData()
          setMessage("Created transaction.")
          setError("")
        }
      })
    }
  }

  return (
    <>
      <Breadcrumb pageName="Form" />

      {error.length > 0 && <AlertError message={error} /> }
      {message.length > 0 && <AlertSuccess message={message} /> }
      <div className="grid grid-cols-1 gap-9 sm:grid-cols-1">
        <div className="flex flex-col gap-9">
          {/* <!-- Input Fields --> */}
          <div className="rounded-[10px] border border-stroke bg-white shadow-1 dark:border-dark-3 dark:bg-gray-dark dark:shadow-card">
            <div className="border-b border-stroke px-6.5 py-4 dark:border-dark-3">
              <h3 className="font-medium text-dark dark:text-white">
                Transaction
              </h3>
            </div>
            <div className="flex flex-col gap-5.5 p-6.5">

              <div>
                <label className="mb-3 block text-body-sm font-medium text-dark dark:text-white">
                  ID
                </label>
                <input
                  required
                  type="text"
                  id="id"
                  value={id}
                  onChange={(e) => setId(e.target.value)}
                  placeholder="1234"
                  className="w-full rounded-[7px] border-[1.5px] border-stroke bg-transparent px-5.5 py-3 text-dark outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-gray-2 dark:border-dark-3 dark:bg-dark-2 dark:text-white dark:focus:border-primary"
                />
              </div>

              <div>
                <select
                  value={transactionType}
                  onChange={(e) => {
                    setTransactionType(e.target.value);
                  }}
                  className="relative z-20 w-full appearance-none rounded-[7px] border border-stroke bg-transparent px-5.5 py-3 outline-none transition focus:border-primary active:border-primary dark:border-dark-3 dark:bg-dark-2 dark:focus:border-primary text-dark dark:text-white"
                >
                  <option value="" disabled className="text-dark-6">
                    TRANSACTION TYPE
                  </option>
                  <option value="transfer" className="text-dark-6">
                    Transfer
                  </option>
                  <option value="deposit" className="text-dark-6">
                    Deposit
                  </option>
                </select>
              </div>

              <div>
                <label className="mb-3 block text-body-sm font-medium text-dark dark:text-white">
                  AMOUNT
                </label>
                <input
                  required
                  type="text"
                  id="amount"
                  value={amount}
                  onChange={(e) => setAmount(e.target.value)}
                  placeholder="200"
                  className="w-full rounded-[7px] border-[1.5px] border-stroke bg-transparent px-5.5 py-3 text-dark outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-gray-2 dark:border-dark-3 dark:bg-dark-2 dark:text-white dark:focus:border-primary"
                />
              </div>

              <div>
                <label className="mb-3 block text-body-sm font-medium text-dark dark:text-white">
                  CURRENCY
                </label>
                <input
                  required
                  type="text"
                  id="currency"
                  value={currency}
                  onChange={(e) => setCurrency(e.target.value)}
                  placeholder="USD"
                  className="w-full rounded-[7px] border-[1.5px] border-stroke bg-transparent px-5.5 py-3 text-dark outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-gray-2 dark:border-dark-3 dark:bg-dark-2 dark:text-white dark:focus:border-primary"
                />
              </div>

              <div>
                <label className="mb-3 block text-body-sm font-medium text-dark dark:text-white">
                  BANK_ACCOUNT_ID
                </label>
                <input
                  required
                  type="text"
                  id="account-id"
                  value={bankAccountId}
                  onChange={(e) => setBankAccountId(e.target.value)}
                  placeholder="1"
                  className="w-full rounded-[7px] border-[1.5px] border-stroke bg-transparent px-5.5 py-3 text-dark outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-gray-2 dark:border-dark-3 dark:bg-dark-2 dark:text-white dark:focus:border-primary"
                />
              </div>
            </div>
          </div>
        </div>
        <button
          type="button"
          onClick={addItem}
          className="bg-primary text-white px-10 py-3.5 lg:px-8 xl:px-10"
        >
          Add User
        </button>
      </div>
    </>
  );
};

export default TransactionForm;
