"use client";
import React, { useState } from 'react';
import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb";
import AlertError from '../Alerts/AlertError';
import {createUser} from "@/api/users";
import AlertSuccess from '../Alerts/AlertSuccess';

const UserForm:  React.FC<{ reloadData: () => void }> = ({ reloadData }) => {

  const [name, setName] = useState<string>('');
  const [email, setEmail] = useState<string>('');
  const [error, setError] = useState<string>('');
  const [message, setMessage] = useState<string>('');

  const addItem = () => {
    if (name && email) {
      createUser(name, email)
      .then(data => {
        if (data == "Error") {
          setError("Error creating the user.")
          setMessage("")
        }
        else {
          reloadData()
          setMessage("Created user.")
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
                User
              </h3>
            </div>
            <div className="flex flex-col gap-5.5 p-6.5">

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
                  placeholder="JOHN RAMBO"
                  className="w-full rounded-[7px] border-[1.5px] border-stroke bg-transparent px-5.5 py-3 text-dark outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-gray-2 dark:border-dark-3 dark:bg-dark-2 dark:text-white dark:focus:border-primary"
                />
              </div>

              <div>
                <label className="mb-3 block text-body-sm font-medium text-dark dark:text-white">
                  EMAIL
                </label>
                <input
                  required
                  type="text"
                  id="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="test@test.com"
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

export default UserForm;
