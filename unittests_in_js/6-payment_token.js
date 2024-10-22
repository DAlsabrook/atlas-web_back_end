function getPaymenTokenFromApi(success) {
    if (success === false) {
        return;
    }
    return Promise.resolve({ data: 'Successful response from the API' })
}

module.exports = getPaymenTokenFromApi;
