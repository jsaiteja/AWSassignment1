import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')


table = dynamodb.create_table(
    TableName='Games',
    KeySchema=[
        {
            'AttributeName': 'gid',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'gname',
            'KeyType': 'RANGE'  #Sort key
        }
           
       
       
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'gid',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'gname',
            'AttributeType': 'S'
        },
        
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
{
    "TableName": "Games",
    "item": {
        "gid": {
            "N": "2"
        },
        "gname": {
            "S": ["Pinball"]
        },
        "publisher": {
            "S": "Amazon DynamoDB"
        },
        "rating": {
            "N": 5
        },
        "release_date": {
            "S": "12may2019"
        },
        "genres": {
            "SS": "[Update, delete]"
        }
    },
}
table.put_item
print("Table status:", table.table_status)