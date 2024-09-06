import { TRANSACTION } from "@/types/transaction";

const ALL_TRANSACTION = "/api/transactions/all";
const CREATE_TRANSACTION = "/api/transactions";
const DELETE_TRANSACTION = "/api/transactions/"

export const getAllTransactions = async (): Promise<TRANSACTION | null> => {
  try {
      const response = await fetch(ALL_TRANSACTION);
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      const data: TRANSACTION = await response.json();
      return data;
  } catch (error) {
      console.error('Fetching data failed:', error);
      return null;
  }
};

export async function createTransaction(id: string, transaction_type: string, currency: string, amount: string, bank_account_id: string) {
    try {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({id: Number(id), transaction_type: transaction_type, amount: Number(amount), currency: currency, bank_account_id: Number(bank_account_id) })
        };
        const response = await fetch(CREATE_TRANSACTION, requestOptions);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return await response.json();
    } catch (error) {
        console.error('Fetching data failed:', error);
        return "Error";
    }
}

export async function deleteTransaction(id: string) {
    try {
        const requestOptions = {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' }
        };
        const response = await fetch(DELETE_TRANSACTION + id, requestOptions);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return await response.json();
    } catch (error) {
        console.error('Fetching data failed:', error);
        return "Error";
    }
}
