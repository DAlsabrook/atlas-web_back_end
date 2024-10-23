import { createClient } from 'redis';

const client = createClient();

// await client.connect();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error('Redis client not connected to the server: ', err);
});

// Close the connection
client.quit();
