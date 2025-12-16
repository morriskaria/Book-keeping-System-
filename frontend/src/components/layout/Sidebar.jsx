import React from 'react';
import { NavLink } from 'react-router-dom';
import {
    LayoutDashboard,
    Users,
    Receipt,
    CreditCard,
    Package,
    FileBarChart,
    Settings,
    LogOut
} from 'lucide-react';

const Sidebar = () => {
    const navItems = [
        { name: 'Dashboard', path: '/', icon: LayoutDashboard },
        { name: 'Patients', path: '/billing/patients', icon: Users },
        { name: 'Billing', path: '/billing/invoices', icon: Receipt },
        { name: 'Payments', path: '/billing/payments', icon: CreditCard }, // Or separate Payments page
        { name: 'Inventory', path: '/inventory', icon: Package },
        { name: 'Reports', path: '/reports', icon: FileBarChart },
    ];

    const adminItems = [
        { name: 'Payroll', path: '/payroll', icon: Users }, // Reusing Users for now, maybe UserCog
        { name: 'Expenses', path: '/expenses', icon: Receipt },
    ];

    return (
        <aside className="fixed left-0 top-0 z-40 h-screen w-64 border-r border-slate-200 bg-white transition-transform dark:border-slate-800 dark:bg-slate-900">
            <div className="flex h-full flex-col">
                {/* Logo Area */}
                <div className="flex h-16 items-center border-b border-slate-200 px-6 dark:border-slate-800">
                    <div className="flex items-center gap-3">
                        <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-medical-blue-600 text-white font-bold">
                            M
                        </div>
                        <span className="text-lg font-bold tracking-tight text-slate-900 dark:text-white">
                            MaturaHMS
                        </span>
                    </div>
                </div>

                {/* Navigation */}
                <div className="flex-1 overflow-y-auto px-3 py-4">
                    <nav className="space-y-1">
                        {navItems.map((item) => (
                            <NavLink
                                key={item.path}
                                to={item.path}
                                className={({ isActive }) =>
                                    `flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium transition-all ${isActive
                                        ? 'bg-medical-blue-50 text-medical-blue-600 dark:bg-medical-blue-900/20 dark:text-medical-blue-500'
                                        : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white'
                                    }`
                                }
                            >
                                <item.icon className="h-5 w-5" />
                                {item.name}
                            </NavLink>
                        ))}

                        <div className="my-4 h-px bg-slate-200 dark:bg-slate-800" />

                        <div className="px-3 text-xs font-semibold uppercase text-slate-400">
                            Admin
                        </div>

                        {adminItems.map((item) => (
                            <NavLink
                                key={item.path}
                                to={item.path}
                                className={({ isActive }) =>
                                    `mt-1 flex items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium transition-all ${isActive
                                        ? 'bg-medical-blue-50 text-medical-blue-600 dark:bg-medical-blue-900/20 dark:text-medical-blue-500'
                                        : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white'
                                    }`
                                }
                            >
                                <item.icon className="h-5 w-5" />
                                {item.name}
                            </NavLink>
                        ))}
                    </nav>
                </div>

                {/* User Profile / Logout */}
                <div className="border-t border-slate-200 p-4 dark:border-slate-800">
                    <button className="flex w-full items-center gap-3 rounded-lg px-3 py-2.5 text-sm font-medium text-slate-600 transition-colors hover:bg-red-50 hover:text-red-600 dark:text-slate-400 dark:hover:bg-red-900/20 dark:hover:text-red-500">
                        <LogOut className="h-5 w-5" />
                        Sign Out
                    </button>
                </div>
            </div>
        </aside>
    );
};

export default Sidebar;
