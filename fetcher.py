from botocore.exceptions import ClientError

class Fetcher:

    def __init__(self, connect_client, target_instance_id) -> None:
        self.connect_client = connect_client
        self.target_instance_id = target_instance_id

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
                PaginationConfig={
                    'MaxItems': 100,
                    'PageSize': 3
                }
            )
            for resp in response_iterator:
                cf_summary_list.append(resp['ContactFlowSummaryList'])
            return cf_summary_list
        except ClientError as e:
            raise Exception(f'boto3 client error in get_contact_flow_summary_list\n{e.__str__()}')
        except Exception as e:
            raise Exception(f'Unexpected error in get_contact_flow_summary_list\n{e.__str__()}')