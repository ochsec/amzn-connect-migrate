from botocore.exceptions import ClientError

class Fetcher:

    def __init__(
        self, 
        connect_client, 
        target_instance_id, 
        pagination_config={
            'MaxItems': 1000,
            'PageSize': 100,
        }):
        self.connect_client = connect_client
        self.target_instance_id = target_instance_id
        self.pagination_config = pagination_config

    def get_contact_flow_summary_list(self):
        cf_summary_list = []
        try:
            paginator = self.connect_client.get_paginator('list_contact_flows')
            response_iterator = paginator.paginate(
                InstanceId=self.target_instance_id,
                ContactFlowTypes=[
                    'CONTACT_FLOW', 'CUSTOMER_QUEUE', 'CUSTOMER_HOLD', 'CUSTOMER_WHISPER',
                    'AGENT_HOLD', 'AGENT_WHISPER', 'OUTBOUND_WHISPER', 'AGENT_TRANSFER',
                    'QUEUE_TRANSFER'
                ],
                PaginationConfig=self.pagination_config
            )
            for resp in response_iterator:
                cf_summary_list.append(resp['ContactFlowSummaryList'])
            return cf_summary_list
        except ClientError as e:
            raise Exception(f'boto3 client error in get_contact_flow_summary_list\n{e.__str__()}')
        except Exception as e:
            raise Exception(f'Unexpected error in get_contact_flow_summary_list\n{e.__str__()}')

    def get_queues_summary_list(self):
        queues_summary_list = []
        try:
            paginator = self.connect_client.get_paginator('list_queues')
            response_iterator = paginator.paginate(
                InstanceId=self.target_instance_id,
                QueueTypes=['STANDARD', 'AGENT'],
                PaginationConfig=self.pagination_config
            )
            for resp in response_iterator:
                queues_summary_list.append(resp['QueueSummaryList'])
            return queues_summary_list
        except ClientError as e:
            raise Exception(f'boto3 client error in get_queues_summary_list\n{e.__str__()}')
        except Exception as e:
            raise Exception(f'Unexpected error in get_queues_summary_list\n{e.__str__()}')

    def get_hours_of_operations_summary_list(self):
        hours_summary_list = []
        try:
            paginator = self.connect_client.get_paginator('list_hours_of_operations')
            response_iterator = paginator.paginate(
                InstanceId=self.target_instance_id,
                PaginationConfig=self.pagination_config
            )
            for resp in response_iterator:
                hours_summary_list.append(resp['HoursOfOperationSummaryList'])
            return hours_summary_list
        except ClientError as e:
            raise Exception(f'boto3 client error in get_hours_of_operations_summary_list\n{e.__str__()}')
        except Exception as e:
            raise Exception(f'Unexpected error in get_hours_of_operations_summary_list\n{e.__str__()}')

    def get_prompts_summary_list(self):
        prompts_summary_list = []
        try:
            paginator = self.connect_client.get_paginator('list_prompts')
            response_iterator = paginator.paginate(
                InstanceId=self.target_instance_id,
                PaginationConfig=self.pagination_config
            )
            for resp in response_iterator:
                prompts_summary_list.append(resp['PromptSummaryList'])
            return prompts_summary_list
        except ClientError as e:
            raise Exception(f'boto3 client error in get_prompts_summary_list\n{e.__str__()}')
        except Exception as e:
            raise Exception(f'Unexpected error in get_prompts_summary_list\n{e.__str__()}')       

    def get_lexbots_summary_list(self):
        lexbots_summary_list = []
        try:
            paginator = self.connect_client.get_paginator('list_lex_bots')
            response_iterator = paginator.paginate(
                InstanceId=self.target_instance_id,
                PaginationConfig={
                    'MaxItems': 200,
                    'PageSize': 25,
                }
            )
            for resp in response_iterator:
                lexbots_summary_list.append(resp['LexBots'])
            return lexbots_summary_list
        except ClientError as e:
            raise Exception(f'boto3 client error in get_lexbots_summary_list\n{e.__str__()}')
        except Exception as e:
            raise Exception(f'Unexpected error in get_lexbots_summary_list\n{e.__str__()}')    
