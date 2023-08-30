import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

const hashData = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

const storeHash = (key, data) => {
  Object.entries(data).forEach(([field, value]) => {
    client.hset(key, field, value, redis.print);
  });
};

const displayHash = (key) => {
  client.hgetall(key, (error, hash) => {
    if (error) {
      console.error(`Error getting hash ${key}: ${error.message}`);
      return;
    }
    console.log(hash);
  });
};

storeHash('HolbertonSchools', hashData);
displayHash('HolbertonSchools');
