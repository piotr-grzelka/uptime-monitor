/* eslint-disable default-param-last */
import { LIST_REQUEST, LIST_SUCCESS, LIST_FAIL, LIST_RESET } from '../types/services';

export const servicesReducer = (state = { OBJECTS: [] }, action) => {
  switch (action.type) {
    case LIST_REQUEST:
      return {
        loading: true,
        OBJECTS: [],
      };

    case LIST_SUCCESS:
      return {
        loading: false,
        success: true,
        OBJECTS: action.payload,
      };

    case LIST_FAIL:
      return {
        loading: false,
        error: action.payload,
        OBJECTS: [],
      };

    case LIST_RESET:
      return {
        OBJECTS: [],
      };

    default:
      return state;
  }
};
