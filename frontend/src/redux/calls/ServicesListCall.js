import { useEffect, memo } from 'react';

import { useDispatch } from 'react-redux';

import { services } from '../actions/servicesActions';

const ServicesListCall = () => {
  // ** Store Vars
  const dispatch = useDispatch();

  // ** Get data on mount
  useEffect(() => {
    dispatch(services());
  }, [dispatch]);

  return null;
};

export default memo(ServicesListCall);
