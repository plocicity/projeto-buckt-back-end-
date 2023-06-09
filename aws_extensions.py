import boto3

s3 = boto3.resource('s3')

const fs = require('fs');
 
async function uploadFile(fileName, filePath, mimeType) {
    const s3 = new AWS.S3({ apiVersion: '2006-03-01', region: process.env.AWS_REGION });
    const fileContent = fs.readFileSync(filePath);
 
    const params = {
        Bucket: NAME.env.AWS_S3_BUCKET,
        Key: fileName,
        Body: fileContent,
        //ContentType: mimeType//geralmente se acha sozinho
    };
 
    const data = await s3.upload(params).promise();
    return data.Location;
}
JavaScript
const AWS = require('aws-sdk');
const fs = require('fs');

async function uploadFile(fileName, filePath, mimeType) {
    const s3 = new AWS.S3({ apiVersion: '2006-03-01', region: process.env.AWS_REGION });
    const fileContent = fs.readFileSync(filePath);

    const params = {
        Bucket: process.env.AWS_S3_BUCKET,
        Key: fileName,
        Body: fileContent,
        //ContentType: mimeType//geralmente se acha sozinho
    };

    const data = await s3.upload(params).promise();
    return data.Location;
}

async function listObjects(filter) {
    const s3 = new AWS.S3({ apiVersion: '2006-03-01', region: process.env.AWS_REGION });
    const params = {
        Bucket: process.env.AWS_S3_BUCKET,
        Prefix: decodeURIComponent(filter)
    };

    const result = await s3.listObjectsV2(params).promise();
    return result.Contents.map(item => item.Key);
}

module.exports = { uploadFile, listObjects }

const AWS = require('aws-sdk');
const fs = require('fs');
 
async function uploadFile(fileName, filePath, mimeType) {
    const s3 = new AWS.S3({ apiVersion: '2006-03-01', region: process.env.AWS_REGION });
    const fileContent = fs.readFileSync(filePath);
 
    const params = {
        Bucket: process.env.AWS_S3_BUCKET,
        Key: fileName,
        Body: fileContent,
        //ContentType: mimeType//geralmente se acha sozinho
    };
 
    const data = await s3.upload(params).promise();
    return data.Location;
}
 
async function listObjects(filter) {
    const s3 = new AWS.S3({ apiVersion: '2006-03-01', region: process.env.AWS_REGION });
    const params = {
        Bucket: process.env.AWS_S3_BUCKET,
        Prefix: decodeURIComponent(filter)
    };
 
    const result = await s3.listObjectsV2(params).promise();
    return result.Contents.map(item => item.Key);
}
 
module.exports = { uploadFile, listObjects }



router.post('/', (req, res, next) => {
  const formidable = require('formidable');
  const form = new formidable.IncomingForm();
 
  form.parse(req, async (err, fields, files) => {
    const s3Client = require('../s3Client');
    const url = await s3Client.uploadFile(files.filetoupload.name, files.filetoupload.path);
    res.send(`File uploaded at ${https://fakestoreapi.com/docs. }`);
  });
});


