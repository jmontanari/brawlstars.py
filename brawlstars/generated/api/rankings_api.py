# coding: utf-8

"""
    Brawl Stars API

    Brawl Stars API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictInt, StrictStr

from typing import List, Optional

from brawlstars.generated.models.club_ranking import ClubRanking
from brawlstars.generated.models.player_ranking import PlayerRanking

from brawlstars.generated.api_client import ApiClient
from brawlstars.generated.api_response import ApiResponse
from brawlstars.generated.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RankingsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_brawler_rankings(self, country_code : Annotated[StrictStr, Field(..., description="Two letter country code, or 'global' for global rankings.")], brawler_id : Annotated[StrictStr, Field(..., description="Identifier of the brawler.")], before : Annotated[Optional[StrictStr], Field(description="Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. ")] = None, after : Annotated[Optional[StrictStr], Field(description="Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. ")] = None, limit : Annotated[Optional[StrictInt], Field(description="Limit the number of items returned in the response.")] = None, **kwargs) -> List[PlayerRanking]:  # noqa: E501
        """Get brawler rankings for a country or global rankings.  # noqa: E501

        Get brawler rankings for a country or global rankings. Brawler identifiers can be found by using the /v1/brawlers API endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_brawler_rankings(country_code, brawler_id, before, after, limit, async_req=True)
        >>> result = thread.get()

        :param country_code: Two letter country code, or 'global' for global rankings. (required)
        :type country_code: str
        :param brawler_id: Identifier of the brawler. (required)
        :type brawler_id: str
        :param before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type before: str
        :param after: Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type after: str
        :param limit: Limit the number of items returned in the response.
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[PlayerRanking]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_brawler_rankings_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_brawler_rankings_with_http_info(country_code, brawler_id, before, after, limit, **kwargs)  # noqa: E501

    @validate_arguments
    def get_brawler_rankings_with_http_info(self, country_code : Annotated[StrictStr, Field(..., description="Two letter country code, or 'global' for global rankings.")], brawler_id : Annotated[StrictStr, Field(..., description="Identifier of the brawler.")], before : Annotated[Optional[StrictStr], Field(description="Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. ")] = None, after : Annotated[Optional[StrictStr], Field(description="Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. ")] = None, limit : Annotated[Optional[StrictInt], Field(description="Limit the number of items returned in the response.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get brawler rankings for a country or global rankings.  # noqa: E501

        Get brawler rankings for a country or global rankings. Brawler identifiers can be found by using the /v1/brawlers API endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_brawler_rankings_with_http_info(country_code, brawler_id, before, after, limit, async_req=True)
        >>> result = thread.get()

        :param country_code: Two letter country code, or 'global' for global rankings. (required)
        :type country_code: str
        :param brawler_id: Identifier of the brawler. (required)
        :type brawler_id: str
        :param before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type before: str
        :param after: Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type after: str
        :param limit: Limit the number of items returned in the response.
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[PlayerRanking], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'country_code',
            'brawler_id',
            'before',
            'after',
            'limit'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_brawler_rankings" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['country_code'] is not None:
            _path_params['countryCode'] = _params['country_code']

        if _params['brawler_id'] is not None:
            _path_params['brawlerId'] = _params['brawler_id']


        # process the query parameters
        _query_params = []
        if _params.get('before') is not None:  # noqa: E501
            _query_params.append(('before', _params['before']))

        if _params.get('after') is not None:  # noqa: E501
            _query_params.append(('after', _params['after']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['JWT']  # noqa: E501

        _response_types_map = {
            '400': "ClientError",
            '403': "ClientError",
            '404': "ClientError",
            '429': "ClientError",
            '500': "ClientError",
            '503': "ClientError",
            '200': "List[PlayerRanking]",
        }

        return self.api_client.call_api(
            '/rankings/{countryCode}/brawlers/{brawlerId}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_club_rankings(self, country_code : Annotated[StrictStr, Field(..., description="Two letter country code, or 'global' for global rankings.")], before : Annotated[Optional[StrictStr], Field(description="Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. ")] = None, after : Annotated[Optional[StrictStr], Field(description="Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. ")] = None, limit : Annotated[Optional[StrictInt], Field(description="Limit the number of items returned in the response.")] = None, **kwargs) -> List[ClubRanking]:  # noqa: E501
        """Get club rankings for a country or global rankings.  # noqa: E501

        Get club rankings for a country or global rankings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_club_rankings(country_code, before, after, limit, async_req=True)
        >>> result = thread.get()

        :param country_code: Two letter country code, or 'global' for global rankings. (required)
        :type country_code: str
        :param before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type before: str
        :param after: Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type after: str
        :param limit: Limit the number of items returned in the response.
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[ClubRanking]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_club_rankings_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_club_rankings_with_http_info(country_code, before, after, limit, **kwargs)  # noqa: E501

    @validate_arguments
    def get_club_rankings_with_http_info(self, country_code : Annotated[StrictStr, Field(..., description="Two letter country code, or 'global' for global rankings.")], before : Annotated[Optional[StrictStr], Field(description="Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. ")] = None, after : Annotated[Optional[StrictStr], Field(description="Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. ")] = None, limit : Annotated[Optional[StrictInt], Field(description="Limit the number of items returned in the response.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get club rankings for a country or global rankings.  # noqa: E501

        Get club rankings for a country or global rankings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_club_rankings_with_http_info(country_code, before, after, limit, async_req=True)
        >>> result = thread.get()

        :param country_code: Two letter country code, or 'global' for global rankings. (required)
        :type country_code: str
        :param before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type before: str
        :param after: Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type after: str
        :param limit: Limit the number of items returned in the response.
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[ClubRanking], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'country_code',
            'before',
            'after',
            'limit'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_club_rankings" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['country_code'] is not None:
            _path_params['countryCode'] = _params['country_code']


        # process the query parameters
        _query_params = []
        if _params.get('before') is not None:  # noqa: E501
            _query_params.append(('before', _params['before']))

        if _params.get('after') is not None:  # noqa: E501
            _query_params.append(('after', _params['after']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['JWT']  # noqa: E501

        _response_types_map = {
            '400': "ClientError",
            '403': "ClientError",
            '404': "ClientError",
            '429': "ClientError",
            '500': "ClientError",
            '503': "ClientError",
            '200': "List[ClubRanking]",
        }

        return self.api_client.call_api(
            '/rankings/{countryCode}/clubs', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_player_rankings(self, country_code : Annotated[StrictStr, Field(..., description="Two letter country code, or 'global' for global rankings.")], before : Annotated[Optional[StrictStr], Field(description="Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. ")] = None, after : Annotated[Optional[StrictStr], Field(description="Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. ")] = None, limit : Annotated[Optional[StrictInt], Field(description="Limit the number of items returned in the response.")] = None, **kwargs) -> List[PlayerRanking]:  # noqa: E501
        """Get player rankings for a country or global rankings.  # noqa: E501

        Get player rankings for a country or global rankings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_player_rankings(country_code, before, after, limit, async_req=True)
        >>> result = thread.get()

        :param country_code: Two letter country code, or 'global' for global rankings. (required)
        :type country_code: str
        :param before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type before: str
        :param after: Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type after: str
        :param limit: Limit the number of items returned in the response.
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[PlayerRanking]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_player_rankings_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_player_rankings_with_http_info(country_code, before, after, limit, **kwargs)  # noqa: E501

    @validate_arguments
    def get_player_rankings_with_http_info(self, country_code : Annotated[StrictStr, Field(..., description="Two letter country code, or 'global' for global rankings.")], before : Annotated[Optional[StrictStr], Field(description="Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. ")] = None, after : Annotated[Optional[StrictStr], Field(description="Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. ")] = None, limit : Annotated[Optional[StrictInt], Field(description="Limit the number of items returned in the response.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get player rankings for a country or global rankings.  # noqa: E501

        Get player rankings for a country or global rankings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_player_rankings_with_http_info(country_code, before, after, limit, async_req=True)
        >>> result = thread.get()

        :param country_code: Two letter country code, or 'global' for global rankings. (required)
        :type country_code: str
        :param before: Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type before: str
        :param after: Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both. 
        :type after: str
        :param limit: Limit the number of items returned in the response.
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(List[PlayerRanking], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'country_code',
            'before',
            'after',
            'limit'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player_rankings" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['country_code'] is not None:
            _path_params['countryCode'] = _params['country_code']


        # process the query parameters
        _query_params = []
        if _params.get('before') is not None:  # noqa: E501
            _query_params.append(('before', _params['before']))

        if _params.get('after') is not None:  # noqa: E501
            _query_params.append(('after', _params['after']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['JWT']  # noqa: E501

        _response_types_map = {
            '400': "ClientError",
            '403': "ClientError",
            '404': "ClientError",
            '429': "ClientError",
            '500': "ClientError",
            '503': "ClientError",
            '200': "List[PlayerRanking]",
        }

        return self.api_client.call_api(
            '/rankings/{countryCode}/players', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
