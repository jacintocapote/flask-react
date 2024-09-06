import { ACCOUNT } from "@/types/account";

const ALL_ACCOUNT = "/api/accounts";
const CREATE_ACCOUNT = "/api/accounts";
const DELETE_ACCOUNT = "/api/accounts/"

export const getAllAccounts = async (): Promise<ACCOUNT> => {
  try {
      const response = await fetch(ALL_ACCOUNT);
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      const data: ACCOUNT  = await response.json();
      return data;
  } catch (error) {
      console.error('Fetching data failed:', error);
      const data_empty: ACCOUNT[] = [];
      return data_empty;
  }
};

export async function createAccount(id: string, account_number: string, balance: number, currency: string, user_id: string) {
    try {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({id: Number(id), account_number: account_number, balance: balance, currency: currency, user_id: Number(user_id) })
        };
        const response = await fetch(CREATE_ACCOUNT, requestOptions);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return await response.json();
    } catch (error) {
        console.error('Fetching data failed:', error);
        return "Error";
    }
}

export async function deleteAccount(id: string) {
    try {
        const requestOptions = {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' }
        };
        const response = await fetch(DELETE_ACCOUNT + id, requestOptions);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return await response.json();
    } catch (error) {
        console.error('Fetching data failed:', error);
        return "Error";
    }
}
