import React, { useState, useEffect } from 'react';
import { format } from 'date-fns';
import { Plus, Search, Filter, MoreVertical, FileText, CheckCircle, Clock } from 'lucide-react';
import api from '../../services/api';

const Invoices = () => {
    const [invoices, setInvoices] = useState([]);
    const [loading, setLoading] = useState(true);
    const [stats, setStats] = useState({ total: 0, pending: 0, paid: 0 });

    useEffect(() => {
        fetchInvoices();
    }, []);

    const fetchInvoices = async () => {
        try {
            // In a real implementation: const response = await api.get('/billing/invoices');
            // Mocking data for now as backend might be empty
            // setInvoices(response.data);

            // MOCK DATA for Visual Verification
            const mockData = [
                { id: 'INV-001', patient_name: 'John Doe', amount: 150.00, status: 'PAID', date: new Date().toISOString() },
                { id: 'INV-002', patient_name: 'Jane Smith', amount: 320.50, status: 'PENDING', date: new Date(Date.now() - 86400000).toISOString() },
                { id: 'INV-003', patient_name: 'Robert Wilson', amount: 45.00, status: 'PAID', date: new Date(Date.now() - 172800000).toISOString() },
            ];
            setInvoices(mockData);
            setStats({
                total: mockData.reduce((acc, curr) => acc + curr.amount, 0),
                pending: mockData.filter(i => i.status === 'PENDING').length,
                paid: mockData.filter(i => i.status === 'PAID').length
            });
        } catch (error) {
            console.error('Error fetching invoices:', error);
        } finally {
            setLoading(false);
        }
    };

    const getStatusColor = (status) => {
        return status === 'PAID'
            ? 'bg-emerald-100 text-emerald-700 dark:bg-emerald-900/30 dark:text-emerald-400'
            : 'bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400';
    };

    return (
        <div className="space-y-6">
            {/* Header */}
            <div className="flex flex-col justify-between gap-4 sm:flex-row sm:items-center">
                <div>
                    <h1 className="text-2xl font-bold text-slate-900 dark:text-white">Invoices</h1>
                    <p className="text-sm text-slate-500 dark:text-slate-400">Manage patient billing and payments.</p>
                </div>
                <button className="flex items-center gap-2 rounded-lg bg-medical-blue-600 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-medical-blue-700">
                    <Plus className="h-4 w-4" />
                    Create Invoice
                </button>
            </div>

            {/* Stats Cards */}
            <div className="grid gap-4 sm:grid-cols-3">
                <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                    <div className="flex items-center gap-3">
                        <div className="rounded-lg bg-blue-50 p-2 text-medical-blue-600 dark:bg-blue-900/20">
                            <FileText className="h-5 w-5" />
                        </div>
                        <div>
                            <p className="text-xs font-medium text-slate-500">Total Revenue</p>
                            <p className="text-lg font-bold text-slate-900 dark:text-white">${stats.total.toFixed(2)}</p>
                        </div>
                    </div>
                </div>
                <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                    <div className="flex items-center gap-3">
                        <div className="rounded-lg bg-amber-50 p-2 text-amber-600 dark:bg-amber-900/20">
                            <Clock className="h-5 w-5" />
                        </div>
                        <div>
                            <p className="text-xs font-medium text-slate-500">Pending</p>
                            <p className="text-lg font-bold text-slate-900 dark:text-white">{stats.pending}</p>
                        </div>
                    </div>
                </div>
                <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm dark:border-slate-800 dark:bg-slate-900">
                    <div className="flex items-center gap-3">
                        <div className="rounded-lg bg-emerald-50 p-2 text-emerald-600 dark:bg-emerald-900/20">
                            <CheckCircle className="h-5 w-5" />
                        </div>
                        <div>
                            <p className="text-xs font-medium text-slate-500">Paid Invoices</p>
                            <p className="text-lg font-bold text-slate-900 dark:text-white">{stats.paid}</p>
                        </div>
                    </div>
                </div>
            </div>

            {/* Table */}
            <div className="rounded-xl border border-slate-200 bg-white shadow-sm dark:border-slate-800 dark:bg-slate-900">
                <div className="flex items-center justify-between border-b border-slate-200 px-6 py-4 dark:border-slate-800">
                    <div className="relative w-64">
                        <Search className="absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-slate-400" />
                        <input
                            type="text"
                            placeholder="Search invoices..."
                            className="w-full rounded-lg border border-slate-200 bg-slate-50 py-2 pl-9 pr-4 text-sm focus:border-medical-blue-500 focus:outline-none dark:border-slate-700 dark:bg-slate-800 dark:text-white"
                        />
                    </div>
                    <button className="flex items-center gap-2 rounded-lg border border-slate-200 px-3 py-2 text-sm font-medium text-slate-600 hover:bg-slate-50 dark:border-slate-700 dark:text-slate-300 dark:hover:bg-slate-800">
                        <Filter className="h-4 w-4" />
                        Filter
                    </button>
                </div>

                <div className="overflow-x-auto">
                    <table className="w-full text-left text-sm">
                        <thead className="bg-slate-50 text-slate-500 dark:bg-slate-800/50 dark:text-slate-400">
                            <tr>
                                <th className="px-6 py-3 font-medium">Invoice ID</th>
                                <th className="px-6 py-3 font-medium">Patient</th>
                                <th className="px-6 py-3 font-medium">Date</th>
                                <th className="px-6 py-3 font-medium">Amount</th>
                                <th className="px-6 py-3 font-medium">Status</th>
                                <th className="px-6 py-3 font-medium">Actions</th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-slate-200 dark:divide-slate-800">
                            {invoices.map((invoice) => (
                                <tr key={invoice.id} className="group hover:bg-slate-50 dark:hover:bg-slate-800/50">
                                    <td className="px-6 py-4 font-medium text-slate-900 dark:text-white">{invoice.id}</td>
                                    <td className="px-6 py-4 text-slate-600 dark:text-slate-300">{invoice.patient_name}</td>
                                    <td className="px-6 py-4 text-slate-500 dark:text-slate-400">
                                        {format(new Date(invoice.date), 'MMM dd, yyyy')}
                                    </td>
                                    <td className="px-6 py-4 font-medium text-slate-900 dark:text-white">
                                        ${invoice.amount.toFixed(2)}
                                    </td>
                                    <td className="px-6 py-4">
                                        <span className={`inline-flex items-center rounded-full px-2.5 py-0.5 text-xs font-medium ${getStatusColor(invoice.status)}`}>
                                            {invoice.status}
                                        </span>
                                    </td>
                                    <td className="px-6 py-4">
                                        <button className="rounded-lg p-1 text-slate-400 hover:bg-slate-100 hover:text-slate-600 dark:hover:bg-slate-700 dark:hover:text-slate-300">
                                            <MoreVertical className="h-4 w-4" />
                                        </button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
};

export default Invoices;
