const readDatabase = require('../utils');

class StudentsController {
    static async getAllStudents(request, response) {
        const fieldObj = await readDatabase('./database.cvs');
        
    }
}
