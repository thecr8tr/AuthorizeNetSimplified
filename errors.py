from authorize_net_response_handler import createTransactionResponse_parser

class Error_E00027(Exception):
    def __init__(self, Response):
        response_dict = createTransactionResponse_parser(Response)
        error_message = 'Response raised error, E00027: \'The transaction was unsuccessful.\'.'
        if response_dict['responseErrorCode']:
            error_message += '\nThis was caused by:'
            for error in response_dict['responseErrorCode']:
                error_message += '\n\tError # {}: \'{}\''.format(error[0], error[1])
        super(Error_E00027, self).__init__(error_message)
