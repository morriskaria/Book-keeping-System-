import React from 'react';

const Dashboard = () => {
    return (
        <div className="space-y-6">
            <div className="flex items-center justify-between">
                <h1 className="text-2xl font-bold text-slate-900 dark:text-white">
                    Dashboard
                </h1>
                <button className="rounded-lg bg-medical-blue-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-medical-blue-700">
                    New Invoice
                </button>
            </div>

            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
                {/* Stats placeholders */}
                {['Total Revenue', 'Active Patients', 'Pending Invoices', 'Low Stock Items'].map((stat) => (
                    <div key={stat} className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                        <h3 className="text-sm font-medium text-slate-500 dark:text-slate-400">{stat}</h3>
                        <p className="mt-2 text-3xl font-bold text-slate-900 dark:text-white">--</p>
                    </div>
                ))}
            </div>

            <div className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                <h2 className="text-lg font-bold text-slate-900 dark:text-white">Recent Activity</h2>
                <div className="mt-4 h-64 flex items-center justify-center text-slate-400">
                    Chart or Table Placeholder
                </div>
            </div>
        </div>
    );
};

export default Dashboard;
