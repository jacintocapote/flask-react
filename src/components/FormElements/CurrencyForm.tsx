"use client";
import React, { useState } from 'react';
import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb";
import {getAllCurrencies, createCurrency} from "@/api/currencies";

const CurrencyForm:  React.FC<{ reloadData: () => void }> = ({ reloadData }) => {

  const [id, setId] = useState<string>('');
  const [name, setName] = useState<string>('');
  const [representation, setRepresentation] = useState<string>('');

  const addItem = () => {
    console.log(getAllCurrencies())
    if (name && id && representation) {
      createCurrency(id, name, representation)
      reloadData()
    }
  }

  return (
    <>
      <Breadcrumb pageName="Form" />

      <div className="grid grid-cols-1 gap-9 sm:grid-cols-1">
        <div className="flex flex-col gap-9">
          {/* <!-- Input Fields --> */}
          <div className="rounded-[10px] border border-stroke bg-white shadow-1 dark:border-dark-3 dark:bg-gray-dark dark:shadow-card">
            <div className="border-b border-stroke px-6.5 py-4 dark:border-dark-3">
              <h3 className="font-medium text-dark dark:text-white">
                Currency
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
                  placeholder="USDC"
                  className="w-full rounded-[7px] border-[1.5px] border-stroke bg-transparent px-5.5 py-3 text-dark outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-gray-2 dark:border-dark-3 dark:bg-dark-2 dark:text-white dark:focus:border-primary"
                />
              </div>

              <div>
                <label className="mb-3 block text-body-sm font-medium text-dark dark:text-white">
                  NAME
                </label>
                <input
                  required
                  type="text"
                  id="name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  placeholder="DOLAR"
                  className="w-full rounded-[7px] border-[1.5px] border-stroke bg-transparent px-5.5 py-3 text-dark outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-gray-2 dark:border-dark-3 dark:bg-dark-2 dark:text-white dark:focus:border-primary"
                />
              </div>

              <div>
                <label className="mb-3 block text-body-sm font-medium text-dark dark:text-white">
                  REPRESENTATION
                </label>
                <input
                  required
                  type="text"
                  id="representation"
                  value={representation}
                  onChange={(e) => setRepresentation(e.target.value)}
                  placeholder="$"
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
          Save
        </button>
      </div>
    </>
  );
};

export default CurrencyForm;
