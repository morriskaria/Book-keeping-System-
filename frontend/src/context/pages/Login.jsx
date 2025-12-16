import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { Lock, Mail, ArrowRight, Activity } from 'lucide-react';

const Login = () => {
    const [email, setEmail] = useState('admin@matura.co');
    const [password, setPassword] = useState('admin123');
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const { login } = useAuth();
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        setError('');

        try {
            await login(email, password);
            navigate('/');
        } catch (err) {
            setError('Invalid credentials. Please try again.');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="flex h-screen w-full overflow-hidden bg-slate-50 dark:bg-slate-900">
            {/* Left Side - Brand & Visual */}
            <div className="relative hidden w-1/2 flex-col justify-between bg-medical-blue-600 p-12 text-white lg:flex">
                <div className="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1505751172876-fa1923c5c528?q=80&w=2070&auto=format&fit=crop')] bg-cover bg-center opacity-20 mix-blend-overlay"></div>
                <div className="relative z-10 flex items-center gap-2">
                    <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-white/20 backdrop-blur">
                        <Activity className="h-6 w-6 text-white" />
                    </div>
                    <span className="text-xl font-bold tracking-wide">MaturaHMS</span>
                </div>

                <div className="relative z-10 max-w-lg">
                    <h1 className="mb-6 text-5xl font-bold leading-tight">
                        Advanced Healthcare Management
                    </h1>
                    <p className="text-lg text-blue-100">
                        Streamline your hospital operations, handle patient billing, and manage inventory with our modern bookkeeping solution.
                    </p>
                </div>

                <div className="relative z-10 text-sm text-blue-200">
                    © 2025 MaturaCo. All rights reserved.
                </div>
            </div>

            {/* Right Side - Login Form */}
            <div className="flex w-full items-center justify-center p-8 lg:w-1/2">
                <div className="w-full max-w-md space-y-8">
                    <div className="text-center lg:text-left">
                        <h2 className="text-3xl font-bold tracking-tight text-slate-900 dark:text-white">
                            Welcome back
                        </h2>
                        <p className="mt-2 text-slate-600 dark:text-slate-400">
                            Please enter your details to access your account.
                        </p>
                    </div>

                    <form onSubmit={handleSubmit} className="space-y-6">
                        <div className="space-y-4">
                            <div>
                                <label className="mb-2 block text-sm font-medium text-slate-700 dark:text-slate-300">
                                    Email Address
                                </label>
                                <div className="relative">
                                    <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
                                        <Mail className="h-5 w-5 text-slate-400" />
                                    </div>
                                    <input
                                        type="email"
                                        value={email}
                                        onChange={(e) => setEmail(e.target.value)}
                                        required
                                        className="block w-full rounded-lg border border-slate-300 bg-white p-2.5 pl-10 text-slate-900 focus:border-medical-blue-500 focus:ring-medical-blue-500 dark:border-slate-600 dark:bg-slate-800 dark:text-white dark:placeholder-slate-400 dark:focus:border-medical-blue-500 dark:focus:ring-medical-blue-500"
                                        placeholder="name@example.com"
                                    />
                                </div>
                            </div>

                            <div>
                                <label className="mb-2 block text-sm font-medium text-slate-700 dark:text-slate-300">
                                    Password
                                </label>
                                <div className="relative">
                                    <div className="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
                                        <Lock className="h-5 w-5 text-slate-400" />
                                    </div>
                                    <input
                                        type="password"
                                        value={password}
                                        onChange={(e) => setPassword(e.target.value)}
                                        required
                                        className="block w-full rounded-lg border border-slate-300 bg-white p-2.5 pl-10 text-slate-900 focus:border-medical-blue-500 focus:ring-medical-blue-500 dark:border-slate-600 dark:bg-slate-800 dark:text-white dark:placeholder-slate-400 dark:focus:border-medical-blue-500 dark:focus:ring-medical-blue-500"
                                        placeholder="••••••••"
                                    />
                                </div>
                            </div>
                        </div>

                        {error && (
                            <div className="rounded-lg bg-red-50 p-4 text-sm text-red-800 dark:bg-red-900/30 dark:text-red-400">
                                {error}
                            </div>
                        )}

                        <button
                            type="submit"
                            disabled={isLoading}
                            className="group flex w-full items-center justify-center gap-2 rounded-lg bg-medical-blue-600 px-5 py-3 text-center text-sm font-medium text-white hover:bg-medical-blue-700 focus:outline-none focus:ring-4 focus:ring-medical-blue-300 disabled:opacity-50 dark:bg-medical-blue-600 dark:hover:bg-medical-blue-700 dark:focus:ring-medical-blue-800"
                        >
                            {isLoading ? 'Signing in...' : 'Sign in to Dashboard'}
                            {!isLoading && <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />}
                        </button>
                    </form>

                    <div className="text-center text-sm text-slate-500 dark:text-slate-400">
                        For access issues, please contact IT Support.
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Login;
