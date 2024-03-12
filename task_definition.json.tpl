[
   {
      "essential": true,
      "name":"fast-api-app",
      "image":"${REPOSITORY_URL}",
      "portMappings":[
         {
            "containerPort":8003,
            "hostPort":8003,
            "protocol":"tcp"
         }
      ],
      "environment":[
         {
            "name":"BROKER_HOST",
            "value":"${BROKER_HOST}"
         },
         {
            "name":"PULSAR_TOKEN",
            "value":"${PULSAR_TOKEN}"
         },         {
            "name":"LEGAL_HOST",
            "value":"${LEGAL_HOST}"
         }
      ],
      "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
          "awslogs-group": "/ecs/fast-api-app",
          "awslogs-region": "us-east-2",
          "awslogs-stream-prefix": "ecs"
        }
      }
   }
]