import React from 'react';
import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';

const Layout = () => {
    return (
        <div className="flex h-screen bg-gray-50 dark:bg-slate-900">
            <Sidebar />
            <main className="flex-1 overflow-auto transition-[margin] ml-64 p-8">
                <div className="mx-auto max-w-7xl">
                    <Outlet />
                </div>
            </main>
        </div>
    );
};

export default Layout;
