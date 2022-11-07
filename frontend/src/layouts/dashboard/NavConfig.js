// component
import Iconify from '../../components/Iconify';

// ----------------------------------------------------------------------

const getIcon = (name) => <Iconify icon={name} width={22} height={22} />;

const navConfig = [
  {
    title: 'dashboard',
    path: '/dashboard',
    icon: getIcon('eva:pie-chart-2-fill'),
  },
  {
    title: 'services',
    path: '/services',
    icon: getIcon('eva:people-fill'),
  },
  {
    title: 'members',
    path: '/members',
    icon: getIcon('eva:people-fill'),
  },
];

export default navConfig;
