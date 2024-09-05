import { USER } from "@/types/user";
import Image from "next/image";
import {getAllUsers} from '@/api/users';

const userData: USER[] = [
  {
    id: "9314e2bf-ae18-442c-8154-bfbb8b97ffb1",
    name: "Google",
    email: "test@test.com"
  },
  {
    id: "9314e2bf-ae18-442c-8154-bfbb8b97ffb1",
    name: "X.com",
    email: "test@test.com"
  },
  {
    id: "9314e2bf-ae18-442c-8154-bfbb8b97ffb1",
    name: "Github",
    email: "test@test.com"
  },
  {
    id: "9314e2bf-ae18-442c-8154-bfbb8b97ffb1",
    name: "Vimeo",
    email: "test@test.com"
  },
  {
    id: "9314e2bf-ae18-442c-8154-bfbb8b97ffb1",
    name: "Facebook",
    email: "test@test.com"
  },
];


const userData1: USER[] = getAllUsers();

const TableUsers = () => {
  return (
    <div className="rounded-[10px] bg-white px-7.5 pb-4 pt-7.5 shadow-1 dark:bg-gray-dark dark:shadow-card">
      <h4 className="mb-5.5 text-body-2xlg font-bold text-dark dark:text-white">
        Users
      </h4>

      <div className="flex flex-col">
        <div className="grid grid-cols-2 sm:grid-cols-4">
          <div className="px-2 pb-3.5">
            <h5 className="text-sm font-medium uppercase xsm:text-base">
              Name
            </h5>
          </div>
          <div className="px-2 pb-3.5 text-center">
            <h5 className="text-sm font-medium uppercase xsm:text-base">
              ID
            </h5>
          </div>
          <div className="px-2 pb-3.5 text-center">
            <h5 className="text-sm font-medium uppercase xsm:text-base">
              Email
            </h5>
          </div>
          <div className="hidden px-2 pb-3.5 text-center sm:block">
            <h5 className="text-sm font-medium uppercase xsm:text-base">
              Actions
            </h5>
          </div>
        </div>

        {userData.map((user, key) => (
          <div
            className={`grid grid-cols-4 sm:grid-cols-4 ${
              key === userData.length - 1
                ? ""
                : "border-b border-stroke dark:border-dark-3"
            }`}
            key={key}
          >
            <div className="flex items-center gap-3.5 px-2 py-4">
              <div className="flex-shrink-0">
                <Image src="/images/user/user-01.png" alt="User" width={48} height={48} />
              </div>
              <p className="hidden font-medium text-dark dark:text-white sm:block">
                {user.name}
              </p>
            </div>

            <div className="flex items-center justify-center px-2 py-4">
              <p className="font-medium text-dark dark:text-white">
                {user.id}
              </p>
            </div>

            <div className="flex items-center justify-center px-2 py-4">
              <p className="font-medium text-green-light-1">
                ${user.email}
              </p>
            </div>

            <div className="hidden items-center justify-center px-2 py-4 sm:flex">
              <p className="font-medium text-dark dark:text-white">
                Edit/Delete
              </p>
            </div>

          </div>
        ))}
      </div>
    </div>
  );
};

export default TableUsers;
