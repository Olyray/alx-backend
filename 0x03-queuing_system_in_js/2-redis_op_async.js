import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const asyncGet = promisify(client.get).bind(client);
const displaySchoolValue = async (schoolName) => {
  try {
    const value = await asyncGet(schoolName);
    console.log(value);
  } catch (error) {
    console.error(`Error getting the value of ${schoolName}`);
  }
};

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
