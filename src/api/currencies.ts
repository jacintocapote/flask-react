import { CURRENCY } from "@/types/currency";

const ALL_CURRENCIES = "/api/currencies";
const CREATE_CURRENCY = "/api/currencies";
const DELETE_CURRENCY = "/api/currencies/"

export const getAllCurrencies = async (): Promise<CURRENCY> => {
  try {
      const response = await fetch(ALL_CURRENCIES);
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      const data: CURRENCY  = await response.json();
      return data;
  } catch (error) {
      console.error('Fetching data failed:', error);
      const data_empty: CURRENCY[] = [];
      return data_empty;
  }
};

export async function createCurrency(id: string, name: string, representation: string) {
    try {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: id, name: name, representation: representation })
        };
        const response = await fetch(CREATE_CURRENCY, requestOptions);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return await response.json();
    } catch (error) {
        console.error('Fetching data failed:', error);
        return [];
    }
}

export async function deleteCurrency(id: string) {
    try {
        const requestOptions = {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' }
        };
        const response = await fetch(DELETE_CURRENCY + id, requestOptions);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return await response.json();
    } catch (error) {
        console.error('Fetching data failed:', error);
        return [];
    }
}
