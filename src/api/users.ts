import { USER } from "@/types/user";

const ALL_USER = "/api/users";
const CREATE_USER = "/api/users";
const DELETE_USER = "/api/user/"

export const getAllUsers = async (): Promise<USER> => {
  try {
      const response = await fetch(ALL_USER);
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      const data: USER  = await response.json();
      return data;
  } catch (error) {
      console.error('Fetching data failed:', error);
      const data_empty: USER[] = [];
      return data_empty;
  }
};

export async function createUser(name: string, email: string) {
    try {
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({name: name, email: email })
        };
        const response = await fetch(CREATE_USER, requestOptions);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return await response.json();
    } catch (error) {
        console.error('Fetching data failed:', error);
        return [];
    }
}

export async function deleteUser(id: string) {
    try {
        const requestOptions = {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' }
        };
        const response = await fetch(DELETE_USER + id, requestOptions);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return await response.json();
    } catch (error) {
        console.error('Fetching data failed:', error);
        return [];
    }
}
