import { createClient } from 'redis';

const client = createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.error('Redis client not connected to the server: ', err);
});

// Subscribe to a channel
client.subscribe('holberton school channel');

// Handle incoming messages
client.on('message', (channel, message) => {
    console.log(`Received message from ${channel}: ${message}`);
    if (message === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel');
        client.quit();
    }
});
