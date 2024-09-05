const ALL_USERS = "/api/users";

export async function getAllUsers() {
  try {
      const response = await fetch(ALL_USERS);
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      return await response.json();
  } catch (error) {
      console.error('Fetching data failed:', error);
      return [];
  }
}